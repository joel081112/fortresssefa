from django.db import models

# Create your models here.
# database stuff
# class base and function
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel


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

    ]

    # what to call the panels on wagtail
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='SEO'),
        ObjectList(Page.settings_panels, heading='Settings', classname='settings'),
        # classname settings adds the cog
    ]

    )


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
    securityText = RichTextField(
        blank=True,
        verbose_name="SecurityText"
    )

    environmentText = RichTextField(
        blank=True,
        verbose_name="EnvironmentText"
    )

    fireText = RichTextField(
        blank=True,
        verbose_name="FireText"
    )

    architecturalText = RichTextField(
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
            'securityText',
            classname="full"
        ),
        FieldPanel(
            'environmentText',
            classname="full"
        ),
        FieldPanel(
            'fireText',
            classname="full"
        ),
        FieldPanel(
            'architecturalText',
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

