from .settings import get_setting


def get_slider_image_dimensions(slides):
    """
    Take the number of slides to show and divide
    `settings.SLICK_SLIDER_CONTAINER_WIDTH` by that amount. Aftwards,
    stretch that size by 50% and return a quadratic form of the image.

    Example:

        - 2 Slides should be displayed
        - `SLICK_SLIDER_CONTAINER_WIDTH` defaults to 1200

        -> This will give us (1200 / 2) = 600 = 600x600 px for each image
    """
    container_width = get_setting('SLICK_SLIDER_CONTAINER_WIDTH')
    return '{w}x{w}'.format(
        w=int(container_width / slides)
    )
