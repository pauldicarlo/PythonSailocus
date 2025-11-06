# paul.dicarlo@gmail.com
import svgwrite

def create_four_sided_sail(points, fileName):

	margin = 20
	canvas_size = (600, 600)
	width, height = canvas_size

	dwg = svgwrite.Drawing(fileName, size=('600px', '600px'))
	cartesian_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")
	dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='darkseagreen'))

	trapezoid = dwg.polygon(
		points=points,
		fill='ivory',
		stroke='black',
		stroke_width=3
	)

	cartesian_group.add(trapezoid)
	dwg.add(cartesian_group)
    
	dwg.save()

peak = (223, 520)
throat = (20, 243)
tack = (10, 10) 
clew = (407, 39) 


four_sided_sail_points = [ peak, throat, tack, clew]


create_four_sided_sail(four_sided_sail_points, "simplesail.svg");

