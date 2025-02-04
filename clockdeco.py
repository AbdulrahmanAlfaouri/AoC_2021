import time
import functools

def clock(func):
	@functools.wraps(func)
	def clocked(*args, **kewargs):
		to = time.time()
		result = func(*args, **kewargs)

		elapsed = time.time() - to
		name = func.__name__
		arg_list = []

		if args:
			arg_list.append(', '.join(repr(arg) for arg in args))

		if kewargs:
			paris = [f"{k}, {w}" in sorted(kewargs.items())]
			arg_lst.append(', '.join(pairs))

		arg_str = ', '.join(arg_list)
		print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result), f"[{elapsed}] {name}({arg_str}) -> res")
		return result
	return clocked