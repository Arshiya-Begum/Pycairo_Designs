import cairo,math

with cairo.SVGSurface("DoubleSlit.svg", 200, 200) as surface:
    context = cairo.Context(surface)

    # Adding black background
    context.rectangle(0, 0, 200, 200)
    context.set_source_rgb(255, 255, 255)
    context.fill()

    # First group of circles
    context.set_source_rgb(0, 0, 0)
    for i in range(0, 30):
        context.set_line_width(0.1+(i/10))
        context.arc(100, 75, 50-(2.5*i), 0, 2*math.pi)
        context.stroke()

    # Second group of circles
    context.set_source_rgb(0, 0, 0)
    for i in range(0, 30):
        context.set_line_width(0.1+(i/10))
        context.arc(100, 120, 50-(2.5*i), 0, 2 * math.pi)
        context.stroke()