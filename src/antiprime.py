## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	d = 1
	n = 0
	while d <= x :
		if (x % d == 0) :
			n = n + 1

		d = d + 1

	x = x - 1
	k = 0
	while x >= 1 and k < n :
		d = 1
		k = 0
        while d <= x :
			if (x % d == 0) :
				k = k + 2

			d = d + 1

		x = x - 1

	if (k < n) :
		return("anti-prime")
	else :
		return("not anti-prime")


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	import sys
	print(main(int(sys.argv[1])))
