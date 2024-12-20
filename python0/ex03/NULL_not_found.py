def NULL_not_found(object: any) -> int:
	match object.__class__.__name__:
		case "NoneType":
			print(f"Nothing: {object} {object.__class__}")
		case "float":
			print(f"Cheese: {object} {object.__class__}")
		case "int":
			print(f"Zero: {object} {object.__class__}")
		case "str":
			if object:
				print("Type not Found")
				return 1
			else:
				print(f"Empty: {object} {object.__class__}")
		case "bool":
			print(f"Fake: {object} {object.__class__}")
	return 0