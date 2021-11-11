Color = require "color"
buffer = require "buffer"
read_shape = require "shapes"

function print_usage()
	print("Usage:")
	print("  default: read from Stream, write to stdout.")
	print("  -r <seed> to use random values")
	print("  -f <filename> to read from file")
	print("  -o <filename> to set output file")
	print("Input format:")
	print("  First line contains number of shapes.")
	print("  In the following lines shapes are entered.")
	print("  All values are separated using whitespace")
	print("Shapes:")
	print("  Circle:    `1 <color> <x> <y> <radius>`")
	print("  Rectangle: `2 <color> <x1> <y1> <x2> <y2>`")
	print("             where (x1, y1) is the left-upper corner")
	print("             and (x2, y2) is the bottom-left.")
	print("  Triangle:  `3 <color> <x1> <y1> <x2> <y2> <x3> <y3>")
	print("Colors:")
	for k, v in pairs(Color) do
		print(string.format("  %d. %s", k, v))
	end
end

function parse_args()
	local result = {
		mirror = nil,
		input = buffer.Stream(io.stdin),
		output = io.stdout
	}
	
	i = 1
	while arg[i] ~= nil do
		option = arg[i]
		i = i + 1

		if option:sub(1,1) ~= "-" or option:len() ~= 2 then
			io.stderr:write("Invalid option: " .. option)
			os.exit(1)
		end

		option = option:sub(2,2)
		if option == "h" then
			print_usage()
			os.exit(0)
		end

		argument = arg[i]
		i = i + 1
		if argument == nil then
			io.stderr:write("Expected an argument after -" .. option)
			os.exit(1)
		end

		err = nil
		if option == "r" then
			math.randomseed(tonumber(argument))
			result.input = buffer.Randomized()
		elseif option == "f" then
			file, err = io.open(argument, "r")
			result.input = buffer.Stream(file)
		elseif option == "m" then
			file, err = io.open(argument, "w")
			result.mirror = file
		elseif option == "o" then
			file, err = io.open(argument, "w")
			result.output = file
		else
			err = "Unknown option: -" .. option
		end
		if err then
			io.stderr:write(err)
			os.exit(1)
		end
	end

	return result
end

function selection_sort_by_perimiter(shapes)
	len = #shapes
	for i = 1,len do
		smallest = i
		perimiter = shapes[i]:perimiter()
		for j = i+1,len do
			p = shapes[j]:perimiter()
			if p < perimiter then
				smallest = j
				perimiter = p
			end
		end
        	shapes[i], shapes[smallest] = shapes[smallest], shapes[i]
	end
end

function main()
	local options = parse_args()
	options.output:setvbuf("full")
	options.input.mirror = options.mirror

	n = options.input:read_int()

	local shapes = {}
	for i = 1,n do
		shapes[i] = read_shape(options.input):read(options.input)
	end

	options.output:write(string.format("Count: %d", #shapes), '\n')

	options.output:write("Data:", '\n')
	for i = 1,n do
		options.output:write(string.format("%d. ", i))
		options.output:write(shapes[i]:show(), '\n')
	end

	selection_sort_by_perimiter(shapes)

	options.output:write("Sorted:", '\n')
	for i = 1,n do
		options.output:write(string.format("%d. ", i))
		options.output:write(shapes[i]:show(), '\n')
	end
end

main()
