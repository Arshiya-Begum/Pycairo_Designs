import cairo

with cairo.SVGSurface("WavetPaper.svg", 200, 200) as surface:
    context = cairo.Context(surface)

    # Adding black background
    context.rectangle(0, 0, 200, 200)
    context.set_source_rgb(255, 255, 255)
    context.fill()

    # Adding wavey lines
    context.set_source_rgb(255, 0, 0)
    context.set_line_width(0.5)
    for i in range(0,35):
        context.move_to(50+(3*i), 20)
        context.line_to(50+(3*i), 125)
        context.stroke()