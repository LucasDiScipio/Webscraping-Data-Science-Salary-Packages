import os
import re
import pickle

POSTS_DIRECTORY_PATH=os.path.join(os.getcwd(), "data", "posts")
EXTRACTED_INFOS_FILE_PATH=os.path.join(os.getcwd(), "data", "posts_extracted_infos.pkl")

def extract_info(post: str, info: str) -> int|float|None:
    m = re.search(rf"{info}.*:(?P<{info}>.*)", post, flags=re.I)
    if m:
        match info:
            case "gross":
                gross_salary = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                gross_salary = gross_salary.group(f"{info}").replace(".", "").replace(",","")
                if len(gross_salary) == 4:
                    return float(gross_salary)
            case "net":
                net_salary = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if net_salary:
                    net_salary = net_salary.group(f"{info}").replace(".", "").replace(",","")
                    if len(net_salary) == 4:
                        return float(net_salary)
            case "experience":
                exp = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if exp:
                    exp = exp.group(f"{info}")
                    if len(exp) <= 3:
                        match exp.count(","):
                            case 1:
                                return(float(exp.replace(",", ".")))
                        return float(exp)
            case "hours":
                hours = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if hours:
                    hours = hours.group(f"{info}")
                    if len(hours) <= 3:
                        match hours.count(","):
                            case 1:
                                return(float(hours.replace(",", ".")))
                        return float(hours)
            case "telework":
                days = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if days:
                    days = days.group(f"{info}")
                    if len(days) <= 3:
                        match days.count(","):
                            case 1:
                                return(float(days.replace(",", ".")))
                        return float(days)
            case "vacation":
                days = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if days:
                    days = days.group(f"{info}")
                    if len(days) <= 3:
                        match days.count(","):
                            case 1:
                                return(int(days.replace(",", ".")))
                        return int(days)
            case "ecocheques":
                ecocheques = re.search(rf"(?P<{info}>\d+(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"))
                if ecocheques:
                    ecocheques = ecocheques.group(f"{info}")
                    if len(ecocheques) <= 4:
                        match ecocheques.count(","):
                            case 1:
                                return(float(ecocheques.replace(",", ".")))
                        return float(ecocheques)
            case "education":
                education = re.search(rf"(?P<{info}>(phd)|(master|msc?)|(bachelor|b[sc][sc]|graduaa?t))", m.group(f"{info}"), flags=re.I)
                if education:
                    return education.group(f"{info}")
            case "employees":
                employees_amount = re.search(rf"(?P<{info}>\d+k?(,\d+)*(\.\d+(e\d+)?)?)", m.group(f"{info}"), flags=re.I)
                if employees_amount:
                    employees_amount = employees_amount.group(f"{info}")\
                                            .replace(".", "").replace(",","")\
                                            .replace("k", "000").replace("K", "000")
                    return int(employees_amount)
    return None

def main():
    posts_info_list = []
    queries = ("data analyst", "data scientist", "data engineer")
    for query in queries:
        query_posts_dir = os.path.join(POSTS_DIRECTORY_PATH, query.replace(" ", "_"))
        for file in os.listdir(query_posts_dir):
            post_info = {
                "job_title": query, 
                "gross_salary": None, 
                "net_salary": None, 
                "experience": None,      
                "working_hours": None,   
                "teleworking_days": None,
                "holidays": None,        
                "ecocheques": None,      
                "education": None,       
                "employees_amount": None,
            }
            with open(os.path.join(query_posts_dir, file), 'r', encoding='utf-8') as post_file:
                post = post_file.read()
                post_info["gross_salary"]     = extract_info(post, info="gross")
                post_info["net_salary"]       = extract_info(post, info="net")
                post_info["experience"]       = extract_info(post, info="experience")
                post_info["working_hours"]    = extract_info(post, info="hours")
                post_info["teleworking_days"] = extract_info(post, info="telework")
                post_info["holidays"]         = extract_info(post, info="vacation")
                post_info["ecocheques"]       = extract_info(post, info="ecocheques")
                post_info["education"]        = extract_info(post, info="education")
                post_info["employees_amount"] = extract_info(post, info="employees")
                posts_info_list.append(post_info)
                
    with open(EXTRACTED_INFOS_FILE_PATH, "wb") as output_file:
        pickle.dump(posts_info_list, output_file) 

if __name__ == "__main__":
    main()