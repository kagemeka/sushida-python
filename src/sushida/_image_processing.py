import logging
import typing

import PIL.Image

_LOGGER = logging.getLogger(__name__)


def _preprocess(image: PIL.Image.Image) -> PIL.Image.Image:
    width, _ = image.size
    PADDING = 76
    image = image.crop((PADDING, 228, width - PADDING, 256))
    image = PIL.ImageOps.grayscale(image)
    image = image.convert("L")
    image = image.point(lut=lambda x: (1 << 8) - 1 if x >= 1 << 7 else 0)
    return PIL.ImageOps.invert(image)


def _optical_character_recognition(image: PIL.Image.Image) -> str:
    import string

    import pytesseract

    WHITELIST = string.ascii_lowercase + string.digits + "!?-,"
    text = pytesseract.image_to_string(
        image,
        config=f"-c tessedit_char_whitelist={WHITELIST}",
    ).strip()
    _LOGGER.info(f"OCR result: {text}")
    return typing.cast(str, text)
