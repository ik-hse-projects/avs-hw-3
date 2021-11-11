colors = require "color"

Circle = require "circle"
Rectangle = require "rectangle"
Triangle = require "triangle"

function read_shape(buffer)
	kind = buffer:read_int(1,3)
	if kind == 1 then
		return Circle
	elseif kind == 2 then
		return Rectangle
	elseif kind == 3 then
		return Triangle
	end
end

return read_shape
