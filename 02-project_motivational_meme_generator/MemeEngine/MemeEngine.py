"""
The MemeGenerator module performs the following responsibilities:
    - Loading of a file from disk
    - Transform image by resizing to a maximum width of 500px while maintaining
        the input aspect ratio
    - Add a caption to an image (string input) with a body and author to a
        random location on the image.
"""

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """MemeEngine class to load inputs, generate memes, and save file."""

    def __init__(self, output_dir: str):
        """
        Initialzie MemeEngine with output directory.

        input: output_dir
            Path to output directory
        """
        self.output_dir = output_dir

    def make_meme(self, image_file, body, author, width=500) -> str:
        """
        Makes a dog meme with a superimposed quote caption.

        input: image_file -
            Path to image file
        input: body -
            Quote body text
        input: author -
            Quote author
        input: width -
            Image width [px]
        """
        try:
            # Load Image and Caption
            img = Image.open(image_file)
            caption = f'"{body}"\n- {author}'
            # test
            image_name = image_file.split("/")[-1]

            # Transform Image
            height = int(img.size[1] / img.size[0] * width)
            img = img.resize((width, height))

            # Add Caption
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(font="./fonts/impact.ttf", size=30)
            x = width * 0.05
            y = height * 0.8
            draw.text(
                (x, y),
                caption,
                font=font,
                fill="white",
                stroke_width=2,
                stroke_fill="black",
                align="right",
            )

            # Save File
            image_name = image_file.split("/")[-1]
            save_file = f"{self.output_dir}/{image_name}"
            img.save(save_file, format="jpeg")

            return save_file

        except FileNotFoundError as error_out:
            print(error_out)
