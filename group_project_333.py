### Data Structure ###

# The processed rows in our data look like this:

import csv

t = 0

rows = []

print("What rows in our processed data look like:")
with open("babynames.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        if t == 0:
            pass
        elif t < 11:
            print('row {} = {}'.format(i, line))
        lal = line[0].split(",")

        if t != 0:
            r = []
            r.append(int(lal[0]))
            r.append(lal[1])
            r.append(lal[2])
            r.append(int(lal[3]))
            r.append(float(lal[4]))
            rows.append(r)
        t += 1

print("Columns and data types for each column/row:")
# The format for each row is [year, gender, name, how many of the name there were in that year, and the proportion that name made up of all names that year].
# Here are the data types for each column:


for i in range(10):
    row = rows[i]
    print("row:", row)
    d = "["
    for elem in row:
        d += str(type(elem)) + ", "
    d += "]"
    print("data types:", d)

# So to surmrise data structure, the year is an int (number), the gender is a string (categorical), the name is a string, 'how many of there were in that year' is an int (number), and the proportion that that name made up of all names that year is a float (number).

### ***Accessing and Playing Around with Data*** ###

# Here we'll print some summaries and findings from the data

name_counts = {}
for row in rows:
    name = row[2]
    if name in name_counts:
        name_counts[name] += row[3]
    else:
        name_counts[name] = row[3]
print("There were", len(list(name_counts.keys())), "unique names")
print()

most_popular_names = []
most_popular_name_counts = sorted(list(name_counts.values()), reverse=True)[0:5]

for key in name_counts:
    if name_counts[key] in most_popular_name_counts:
        most_popular_names.append(key)

print("Of these names, these were the five most popular names of all time (in no particular order):")
for n in most_popular_names:
    print(n, "with", name_counts[n], "instances")
print()
print("Here are the five most popular female names of all time (in no particular order):")

name_counts_female = {}
name_counts_male = {}
for row in rows:
    name = row[2]
    if row[1] == 'F':
        if name in name_counts_female:
            name_counts_female[name] += row[3]
        else:
            name_counts_female[name] = row[3]
    else:
        if name in name_counts_male:
            name_counts_male[name] += row[3]
        else:
            name_counts_male[name] = row[3]

most_popular_names_female = []
most_popular_name_counts_female = sorted(list(name_counts_female.values()), reverse=True)[0:5]

for key in name_counts_female:
    if name_counts_female[key] in most_popular_name_counts_female:
        most_popular_names_female.append(key)
for n in most_popular_names_female:
    print(n, "with", name_counts[n], "instances")

# Here are the most popular names with representation in both genders, where we're starting to explore the impact
# of evolving attitudes and beliefs surrounding gender identity:
print("Here are some of the names with representation in both genders:")
print("""we're starting to explore the impact
# of evolving attitudes and beliefs surrounding gender identity:""")
male_names = list(name_counts_male.keys())
female_names = list(name_counts_female.keys())
overlap_names = list(set(male_names).intersection(female_names))

name_ratios = {} # key of name, value of tuple (MALE_COUNT, FEMALE_COUNT)
for name in overlap_names:
    if name_counts_male[name] > 10000 and name_counts_female[name] > 10000:
        name_ratios[name] = (name_counts_male[name], name_counts_female[name])
        # print(name, "with", name_counts_male[name], "males named this and", name_counts_female[name], "females named this.")
#
# print("And here are how many 'unisex' names (represented by both genders) there were in 1900 vs. 2015:")
# name_counts_female_1900 = {}
# name_counts_male_1900 = {}
# name_counts_female_2015 = {}
# name_counts_male_2015 = {}
# for row in rows:
#     name = row[2]
#     if row[0] == 1900:
#         if row[1] == 'F':
#             if name in name_counts_female_1900:
#                 name_counts_female_1900[name] += row[3]
#             else:
#                 name_counts_female_1900[name] = row[3]
#         else:
#             if name in name_counts_male_1900:
#                 name_counts_male_1900[name] += row[3]
#             else:
#                 name_counts_male_1900[name] = row[3]
#     if row[0] == 2015:
#         if row[1] == 'F':
#             if name in name_counts_female_2015:
#                 name_counts_female_2015[name] += row[3]
#             else:
#                 name_counts_female_2015[name] = row[3]
#         else:
#             if name in name_counts_male_2015:
#                 name_counts_male_2015[name] += row[3]
#             else:
#                 name_counts_male_2015[name] = row[3]
#
# male_names_1900 = list(name_counts_male_1900.keys())
# female_names_1900 = list(name_counts_female_1900.keys())
# overlap_names_1900 = list(set(male_names_1900).intersection(female_names_1900))
# print("Number of 'unisex names' in 1900:", len(overlap_names_1900))
#
# male_names_2015 = list(name_counts_male_2015.keys())
# female_names_2015 = list(name_counts_female_2015.keys())
# overlap_names_2015 = list(set(male_names_2015).intersection(female_names_2015))
# print("Number of 'unisex names' in 2015:", len(overlap_names_2015))
#
print("this many names:", len(list(name_ratios.keys())))

# get female count of the year, male count of the year

# data = []
# for row in rows:
#     if row[2] in name_ratios:
#         data.append(row)
#
year_name_counts = {}
# key of year, key of dictionary with key of name, tuple of (female, male)
for row in rows:
    year = row[0]
    sex = row[1]
    name = row[2]
    count = row[3]

    if year in year_name_counts:
        if name in year_name_counts[year]:
            if sex == 'F':
                year_name_counts[year][name][0] = count
            else:
                year_name_counts[year][name][1] = count

        else:
            year_name_counts[year][name] = [0, 0]
            if sex == 'F':
                year_name_counts[year][name][0] = count
            else:
                year_name_counts[year][name][1] = count
    else:
        year_name_counts[year] = {}
        year_name_counts[year][name] = [0, 0]
        if sex == 'F':
            year_name_counts[year][name][0] = count
        else:
            year_name_counts[year][name][1] = count

# print(repr(year_name_counts))
data = []
for year in list(year_name_counts.keys()):
    for name in list(year_name_counts[year].keys()):
        if name in name_ratios:
            row = (year, name, year_name_counts[year][name][0], year_name_counts[year][name][1])
            data.append(row)

print(repr(name_ratios))


with open('babynames_unisex.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    # writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

