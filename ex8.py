formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
# True and False do not need quotation marks like "one"
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#the third line only prints with "" because it is %r and that is more efficient!
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)	