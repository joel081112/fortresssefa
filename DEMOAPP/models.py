import json

from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import TextField, CharField
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re
from django import template

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel, FieldRowPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable, ClusterableModel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.users.forms import UserEditForm, UserCreationForm
from wagtail.images.blocks import ImageChooserBlock

from .blocks import CardBlock, QuestionBlock, ImageTextsBlock, ImageTextBlock, ArticleBlock, LocationCardBlock, \
    ButtonLinksBlock, InlineVideoBlock, ImageTextArticleBlock
from django.conf import settings
from django.conf.urls.static import static
from ckeditor.fields import RichTextField as rtf


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(WagtailCaptchaEmailForm):
    # the landing page code
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    # the labels code
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], "Email"),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')
        date_sorted_posts = sorted(all_posts, key=lambda p: p.specific.date, reverse=True)
        # Paginate all posts by 5 per page
        paginator = Paginator(date_sorted_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([FieldPanel('date'),
                         FieldPanel('intro'),
                         FieldPanel('body', classname="full")],
                        heading="blogpage Options"
                        ),

        MultiFieldPanel(
            [InlinePanel('blogpage_images', max_num=30, min_num=0, label="blogpage images")],
            heading="blogpage Images"
        ),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='blogpage_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ContactUs(Page):
    content = StreamField(
        [
            ("locations", LocationCardBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class About(Page):
    firstBox = RichTextField(
        blank=True, verbose_name="First"
    )
    secondBox = RichTextField(
        blank=True, verbose_name="Second"
    )
    extra = RichTextField(blank=True)
    brands = RichTextField(blank=True)
    brand = StreamField(
        [
            ("brands", ImageTextBlock()),
        ],
        null=True,
        blank=True,
    )
    timeline = StreamField(
        [
            ("timeline", ImageTextsBlock()),
        ],
        null=True,
        blank=True,
    )
    clientIntro = RichTextField(
        blank=True, verbose_name="Client Intro"
    )

    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('firstBox'),
                FieldPanel('secondBox')
            ],
            heading="About Intro Boxes"
        ),
        FieldPanel('extra'),
        FieldPanel('brands'),
        StreamFieldPanel("brand"),
        MultiFieldPanel(
            [InlinePanel('global_partner_images', max_num=30, min_num=1, label="global partner images")],
            heading="global partner Images"
        ),
        StreamFieldPanel("timeline"),
        MultiFieldPanel(
            [
                FieldPanel('clientIntro'),
                InlinePanel('client_images', max_num=30, min_num=1, label="client images")],
            heading="clients"
        ),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class AboutGalleryImage(Orderable):
    page = ParentalKey(About, on_delete=models.CASCADE, related_name='client_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

    class AboutGlobalImage(Orderable):
        page = ParentalKey(About, on_delete=models.CASCADE, related_name='global_partner_images')
        image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=False,
            on_delete=models.CASCADE,
            related_name='+'
        )

        panels = [
            ImageChooserPanel('image'),
        ]


class Products(Page):
    alert = RichTextField(
        blank=True, verbose_name="Products Alert"
    )
    showcase = StreamField(
        [
            ("video", InlineVideoBlock()),
        ],
        null=True,
        blank=True,
    )

    content = StreamField(
        [
            ("links", ButtonLinksBlock()),
        ],
        null=True,
        blank=True,
    )

    # content tab panels
    content_panels = Page.content_panels + [
        StreamFieldPanel("showcase"),
        MultiFieldPanel(
            [
                FieldPanel('alert'),
                InlinePanel('products_images', max_num=30, min_num=0, label="products images")],
            heading="products overview"
        ),
        StreamFieldPanel("content"),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class ProductsGalleryImage(Orderable):
    page = ParentalKey(Products, on_delete=models.CASCADE, related_name='products_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class NotFound(Page):
    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )

    class PermissionDenied(Page):
        # content tab panels
        content_panels = Page.content_panels + [

        ]

        # what to call the panels on wagtail
        edit_handler = TabbedInterface([
            ObjectList(content_panels, heading='Content'),
            ObjectList(Page.promote_panels, heading='SEO'),
            ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
            # classname settings adds the cog
        ]

        )


class Temp(Page):
    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class Privacy(Page):
    intro = RichTextField(
        blank=True,  # required field or not
        verbose_name="Intro"  # called on wagtail site
    )

    content_panels = Page.content_panels + [

        FieldPanel(
            'intro',
            classname="full"
        ),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class FAQ(Page):
    content = StreamField(
        [
            ("questions", QuestionBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class DeleteAccount(Page):
    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class OverviewAccount(Page):
    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class UserDeleted(Page):
    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class Legal(Page):
    # content tab panels
    intro = RichTextField(
        blank=True,  # required field or not
        verbose_name="Intro"  # called on wagtail site
    )
    content = StreamField(
        [
            ("legal", ArticleBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [

        FieldPanel(
            'intro',
            classname="full"
        ),
        MultiFieldPanel(
            [InlinePanel('legal_pdf', max_num=20, min_num=0, label="legal pdf")],
            heading="legal pdf"
        ),
        MultiFieldPanel(
            [InlinePanel('legal_images', min_num=0, label="legal images")],
            heading="legal Images"
        ),
        StreamFieldPanel("content"),

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class LegalGalleryImage(Orderable):
    page = ParentalKey(Legal, on_delete=models.CASCADE, related_name='legal_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=30)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class LegalDownloads(Orderable):
    page = ParentalKey(Legal, on_delete=models.CASCADE, related_name='legal_pdf')
    legal_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('caption'),
        DocumentChooserPanel('legal_pdf'),
    ]


class Cookies(Page):
    # content tab panels
    intro = RichTextField(
        blank=True,  # required field or not
        verbose_name="Intro"  # called on wagtail site
    )

    content_panels = Page.content_panels + [

        FieldPanel(
            'intro',
            classname="full"
        ),

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class Servicing(Page):
    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    intro = StreamField(
        [
            ("intro", ImageTextArticleBlock()),
        ],
        null=True,
        blank=True,
    )

    # content tab panels
    content_panels = Page.content_panels + [
        StreamFieldPanel('intro')
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class ProTec(Page):
    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    intro = RichTextField(blank=True)
    location = RichTextField(blank=True)

    # content tab panels
    content_panels = Page.content_panels + [
        FieldPanel(
            'intro',
            classname="full"
        ),
        MultiFieldPanel(
            [InlinePanel('protec_images', min_num=0, label="protec images")],
            heading="protec Images"
        ),
        FieldPanel(
            'location',
            classname="full"
        ),

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class ProTecGalleryImage(Orderable):
    page = ParentalKey(ProTec, on_delete=models.CASCADE, related_name='protec_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ArchitectPage(Page):
    content = StreamField(
        [
            ("cards", CardBlock()),
        ],
        null=True,
        blank=True,
    )

    # content tab panels
    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ])


class DoorSteel(Page):
    alertText = CharField(blank=True, max_length=250)
    alertInfo = RichTextField(
        blank=True, verbose_name="Alert Info"
    )
    general = RichTextField(
        blank=True,  # required field or not
        verbose_name="General"  # called on wagtail site
    )

    hardware = RichTextField(
        blank=True,  # required field or not
        verbose_name="Hardware Options"  # called on wagtail site
    )

    doorOptions = RichTextField(
        blank=True,  # required field or not
        verbose_name="Door Options"  # called on wagtail site
    )

    dimensions = RichTextField(
        blank=True,  # required field or not
        verbose_name="Door Dimensions"  # called on wagtail site
    )

    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('alertText'),
                FieldPanel('alertInfo'),
                InlinePanel('steelDoor_images', max_num=30, min_num=0, label="steelDoor images")],
            heading="Steel Door Header"
        ),
        MultiFieldPanel(
            [InlinePanel('steelDoor_pdf', max_num=20, min_num=0, label="steelDoor pdf")],
            heading="steelDoor pdf"
        ),
        MultiFieldPanel(
            [
                FieldPanel('general', classname="full", ),
                FieldPanel('hardware', classname="full", ),
                FieldPanel('doorOptions', classname="full", ),
                FieldPanel('dimensions', classname="full", )],
            heading="Steel Door info"
        ),
    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class SteelDoorDownloads(Orderable):
    page = ParentalKey(DoorSteel, on_delete=models.CASCADE, related_name='steelDoor_pdf')
    steelDoor_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('caption'),
        DocumentChooserPanel('steelDoor_pdf'),
    ]


class SteelDoorGalleryImage(Orderable):
    page = ParentalKey(DoorSteel, on_delete=models.CASCADE, related_name='steelDoor_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class SiteMap(Page):
    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class HomePage(Page):
    # decide whats editable in backend
    # do this instead of text field
    # you can bold different words in it
    # works like micro word
    intro = RichTextField(
        blank=True,  # required field or not
        verbose_name="Intro"  # called on wagtail site
    )
    security = RichTextField(
        blank=True,
        verbose_name="SecurityText"
    )

    environment = RichTextField(
        blank=True,
        verbose_name="EnvironmentText"
    )

    fire = RichTextField(
        blank=True,
        verbose_name="FireText"
    )

    architectural = RichTextField(
        blank=True,
        verbose_name="ArchitecturalText"
    )

    search_fields = Page.search_fields + [
        index.SearchField(
            'intro',
        ),
        index.SearchField(
            'security',
        ),
        index.SearchField(
            'environment',
        ),
        index.SearchField(
            'fire',
        ),
        index.SearchField(
            'architectural',
        ),

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [
        FieldPanel(
            'intro',
            classname="full"
        ),
        FieldPanel(
            'security',
            classname="full"
        ),
        FieldPanel(
            'environment',
            classname="full"
        ),
        FieldPanel(
            'fire',
            classname="full"
        ),
        FieldPanel(
            'architectural',
            classname="full"
        ),
        InlinePanel(
            'homepage_images',
            label="Homepage images"
        ),

        # InlinePanel(
        #     'security_images',
        #     label="Security images"
        # ),

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='homepage_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.TextField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


# end wagtail models


# start django models
class Type(models.Model):
    """Group type of product."""

    name = models.CharField(max_length=30, default='', blank=False)

    class Meta:
        """Meta class."""

        unique_together = (("name",),)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Make a door page."""

    name = models.CharField(max_length=40, default='')
    heading = models.ForeignKey(
        Type, on_delete=models.SET_NULL,
        blank=True,
        null=True, default='', help_text='Choose a group this belongs to'
    )
    product_picture = models.ImageField(
        null=True, blank=True,
        upload_to='original_images/'
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    information = rtf(blank=True, null=True)
    pdf = models.FileField(
        upload_to='documents/',
        null=True, blank=True
    )

    class Meta:
        """Meta class."""

        unique_together = (("name",),)

    def __str__(self):
        return str(self.name)
