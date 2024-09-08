import json
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("template/"))
template = environment.get_template("index.html")

config_file = open('data/configure.json')
config_data = json.load(config_file)

dates_file = open('data/important_dates.json')
dates_data = json.load(dates_file)


print("index.html generated")
dic = []
i = 0

for d in dates_data:
    bad_date = d['date']
    nice_date = str(bad_date[2]) + "." + str(bad_date[1]+1) + "." + str(bad_date[0])
    i += 1

    new_id = "c" + str(i)

    dic.append({
        "day" : nice_date, 
        "id" : new_id,
        "description" : d["description"]
        })

index_cnt = template.render(days = dic, reg_link = config_data['registration form'])

with open("src/scripts/calendar.js") as f:
    lines = f.readlines()

new_line = """const interesting_dates = ["""
                                         #new Date(2024, 7, 23), new Date(2024, 7, 28), new Date(2024, 8, 1), new Date(2024, 8, 1), new Date(2024, 8, 3)];
i = 0
for d in dates_data:
    day = d['date']
    i += 1
    new_line += f"new Date({day[0]}, {day[1]}, {day[2]})"
    if i < len(dates_data):
        new_line += ", "
new_line += "];\n"

lines[0] = new_line


with open("src/scripts/calendar.js", "w") as f:
    f.writelines(lines)

with open("index.html", mode="w", encoding="utf-8") as m:
    m.write(index_cnt)

print("=========================== INDEX.HTML PRINTED ===========================")

programme_file = open('data/programme.json')
programme_data = json.load(programme_file)

template = environment.get_template("programme.html")

programme_cnt = template.render(days = programme_data)

with open("programme.html", mode="w", encoding="utf-8") as m:
    m.write(programme_cnt)

print("=========================== PROGRAMME.HTML PRINTED ===========================")

template = environment.get_template("committee.html")

committee_cnt = template.render(scientific=config_data['scientific committee'], organizing=config_data['organizing committee'])

with open("committee.html", mode="w", encoding="utf-8") as m:
    m.write(committee_cnt)

print("=========================== COMMITTEE.HTML PRINTED ===========================")

# f = open('data/programme.json')
# txt = json.load(f)
#
#
# cnt = template.render(days=txt)
#
# with open("programme.html", mode="w", encoding="utf-8") as m:
#     m.write(cnt)
#
# print("programme.html generated")
#
# dates_file = open('data/important_dates.json')
# dates_json = json.load(dates_file)
# template = environment.get_template("index.html")
#
# dic = []
# i = 0
#
# for d in dates_json:
#     bad_date = d['date']
#     nice_date = str(bad_date[2]) + "." + str(bad_date[1]+1) + "." + str(bad_date[0])
#     i += 1
#
#     new_id = "c" + str(i)
#
#     dic.append({
#         "day" : nice_date, 
#         "id" : new_id,
#         "description" : d["description"]
#         })
#
# cnt = template.render(days = dic)
#
# with open("src/scripts/calendar.js") as f:
#     lines = f.readlines()
#
# new_line = """const interesting_dates = ["""
#                                          #new Date(2024, 7, 23), new Date(2024, 7, 28), new Date(2024, 8, 1), new Date(2024, 8, 1), new Date(2024, 8, 3)];
# i = 0
# for d in dates_json:
#     day = d['date']
#     i += 1
#     new_line += f"new Date({day[0]}, {day[1]}, {day[2]})"
#     if i < len(dates_json):
#         new_line += ", "
# new_line += "];\n"
#
# lines[0] = new_line
#
#
# with open("src/scripts/calendar.js", "w") as f:
#     f.writelines(lines)
#
# with open("index.html", mode="w", encoding="utf-8") as m:
#     m.write(cnt)
#
# print("index.html generated")
#
# config_file = open('data/configure.json')
# config_json = json.load(config_file)
# template = environment.get_template("committee.html")
#
# cnt = template.render(scientific=config_json['scientific committee'], organizing=config_json['organizing committee'])
#
# with open("committee.html", mode="w", encoding="utf-8") as m:
#     m.write(cnt)
# print("committee.html generated")
#
# template = environment.get_template("registration.html")
# cnt = template.render(registration=config_json['registration form'])
#
# with open("registration.html", mode="w", encoding="utf-8") as m:
#     m.write(cnt)
# print("registration.html generated")
