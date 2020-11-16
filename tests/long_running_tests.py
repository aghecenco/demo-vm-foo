PERF_DROP=3 # percentages; modify this to change the test behavior.

THRESHOLD=2 # percentages

if PERF_DROP < 0:
    print("Performance INCREASED by {}%".format(-PERF_DROP))
elif PERF_DROP == 0:
    print("Performance DID NOT CHANGE")
else:
    print("Performance DECREASED by {}&".format(PERF_DROP))

# We can only return PASS or FAIL, it's a test after all.
# The only FAIL condition is decreasing performance by >THRESHOLD.
# Everything else is PASS.
if PERF_DROP > THRESHOLD:
    exit(1)
