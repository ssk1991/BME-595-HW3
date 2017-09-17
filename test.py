from logic_gates import XOR
from logic_gates import AND
from logic_gates import OR
from logic_gates import NOT


And = AND()
print("And(False,False)", And(False, False), "\n", "And(False,True)", And(False, True), "\n", "And(True,False)", And(True, False), "\n", "And(True,True)", And(True, True), "\n",)

Or = OR()
print("Or(False,False)", Or(False, False), "\n", "Or(False,True)", Or(False, True), "\n", "Or(True,False)", Or(True, False), "\n", "Or(True,True)", Or(True, True), "\n",)

Not = NOT()
print("Not(False)", Not(False), "\n", "Not(True)", Not(True), "\n",)

XOr = XOR()
print("XOr(False,False)", XOr(False, False), "\n", "XOr(False,True)", XOr(False, True), "\n", "XOr(True,False)", XOr(True, False), "\n", "XOr(True,True)", XOr(True, True), "\n",)
