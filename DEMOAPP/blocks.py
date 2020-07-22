"""StreamFields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add your additional")

    class Meta:
        template = "title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    image = ImageChooserBlock(required=False, help_text="Add your Image")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("document", DocumentChooserBlock(required=True))
            ]
        )
    )

    class Meta:
        template = "card_block.html"
        icon = "edit"
        label = "Product Cards"


class ImageTextsBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text="Add your Image")
    title = blocks.CharBlock(required=True, help_text="Add your title")

    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("info", blocks.RichTextBlock(required=True, max_length=300)),
            ]
        )
    )

    class Meta:
        template = "timeline_block.html"
        icon = "edit"
        label = "Extra Timeline"


class ImageTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text="Add your Image")
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.CharBlock(required=True, help_text="Add your detail")

    class Meta:
        template = "image_text_block.html"
        icon = "edit"
        label = "Image and Text"


class QuestionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your main title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("question", blocks.CharBlock(require=True, max_length=100)),
                ("answer", blocks.RichTextBlock(required=True, max_length=300)),
            ]
        )
    )

    class Meta:
        template = "question_block.html"
        icon = "edit"
        label = "New Question"


class ButtonLinksBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(require=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url",
                 blocks.URLBlock(required=False, help_text="If the button above is selected, that will be used first")),
                ("document", DocumentChooserBlock(required=True))
            ]
        )
    )


