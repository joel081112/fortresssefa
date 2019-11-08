from django.db import models
# Create your models here.
# database stuff
# class base and function
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


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
        # Paginate all posts by 4 per page
        paginator = Paginator(date_sorted_posts, 4)
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
            [InlinePanel('blogpage_images', max_num=30, min_num=1, label="blogpage images")],
            heading="blogpage Images"
        ),
    ]


class BlogPageGalleryImage(Orderable):
    """Between 1 and 30 images for the blog page carousel."""

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


class About(Page):
    search_fields = Page.search_fields + [

    ]  # these are if adding a search to the website

    # content tab panels
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel('client_images', max_num=30, min_num=1, label="client images")],
            heading="client Images"
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


class Products(Page):
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


class ProTec(Page):
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


class DoorSpeed(Page):
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


class DoorSectional(Page):
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


class DoorSteel(Page):
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


class ShuttersCommercial(Page):
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


class ShuttersFireCurtains(Page):
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


class ShuttersFireShutters(Page):
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


class ShuttersIndustrial(Page):
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


class ShuttersInsulated(Page):
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


class ShuttersSmokeCurtains(Page):
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


class OtherFortressTrellidor(Page):
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


class OtherCrimeGuardScreen(Page):
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


class OtherLoadingBays(Page):
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


class OtherPartitionScreens(Page):
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


class OtherSecurityGates(Page):
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
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
