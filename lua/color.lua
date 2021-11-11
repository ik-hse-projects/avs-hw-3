local colors = {
	[0] = 'red',
	[1] = 'orange',
	[2] = 'yellow',
	[3] = 'green',
	[4] = 'light_blue',
	[5] = 'blue',
	[6] = 'purple'
}

function colors:read(buffer)
	local num = buffer:read_int(0, 6)
	return self[num]
end

return colors
