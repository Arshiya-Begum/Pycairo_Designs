import cairo

with cairo.SVGSurface("ScanLines.svg", 200, 200) as surface:
    context = cairo.Context(surface)

    # Adding black background
    context.rectangle(0, 0, 200, 200)
    context.set_source_rgb(0, 0, 0)
    context.fill()

    # Adding Red line
    context.set_source_rgb(255, 0, 0)
    context.set_line_width(0.5)
    for i in range(0,35):
        context.move_to(50+(3*i), 20)
        context.line_to(50+(3*i), 125)
        context.stroke()

    # Adding green line
    context.set_source_rgb(0, 153, 0)
    context.set_line_width(0.5)
    for i in range(0, 35):
            context.move_to(24 + (3 * i), 40)
            context.line_to(24 + (3 * i), 145)
            context.stroke()

    # Adding green line
    context.set_source_rgb(0, 0, 255)
    context.set_line_width(0.5)
    for i in range(0, 35):
        context.move_to(75 + (3 * i), 70)
        context.line_to(75 + (3 * i), 175)
        context.stroke()