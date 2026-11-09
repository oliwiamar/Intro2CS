plan = ["gym","work", "sleep", "read", "walk"]
print(plan)

print(plan[0])
print(plan[-1])

print(plan[1:4])
print(plan[::-1])

plan[1] = "shopping"
print(plan)

plan.append("shopping")
plan.insert(0, "cooking")
print(plan)

plan.remove("walk")

weekend = ["partying", "swimming"]
final_plan = plan + weekend
print(final_plan)