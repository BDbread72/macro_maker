import sys
import subprocess
import os, json, time, random
try:
    import pyautogui as pt
except:
    subprocess.check_call([sys.executable,"-m","pip","install","--upgrade","pip"])
    subprocess.check_call([sys.executable,"-m","pip","install","--upgrade","pyautogui"])
class cmd:
    def console(text):
        print(">>> "+str(text))
    def find_file(path):
        return os.path.exists(path)
    def split_text(text):
        result = []
        temp = ""
        flag = False
        for c in text:
            if c == " " and not flag:
                result.append(temp)
                temp = ""
            elif c == "'":
                flag = not flag
            else:
                temp += c
        if temp:
            result.append(temp)
        return result
    def read_file(file):
        with open('%s' %file, 'r', encoding="UTF-8") as f:
            res = json.load(f)
        return res
    def compare_as_var(a,b,comparance):
        a=int(a)
        b=int(b)
        if comparance=="==":
            if a==b:
                return True
            else:
                return False
        if comparance=="!=":
            if a!=b:
                return True
            else:
                return False
        if comparance==">":
            if a>b:
                return True
            else:
                return False
        if comparance=="<":
            if a<b:
                return True
            else:
                return False
        if comparance==">=":
            if a>=b:
                return True
            else:
                return False
        if comparance=="<=":
            if a<=b:
                return True
            else:
                return False
    def calculate(a,b,calculation):
        res=a,calculation,b
        return eval(res)
        

running=False
class macro:
    def run_code(command_list):
        global running
        for i in command_list:
            command = cmd.split_text(i)
            if command[0] == "click":
                pt.click()
                cmd.console("click!")
            if command[0] == "mouse_to_img":
                wh=True
                while wh:
                    ins=pt.locateOnScreen("projects\\%s\\imgs\\%s" %(project_name,project_json["macro"]["imgs"][command[1]]), confidence=settings['confidence'], grayscale=True)
                    #cmd.console("move to "+str(ins))
                    if ins is not None:
                        wh=False
                pt.moveTo(ins)
                cmd.console("move to "+str(ins))
            if command[0] == "wait":
                time.sleep(float(command[1]))
            if command[0] =="move_to":
                pt.moveTo(float(command[1]), float(command[2]))
            if command[0] =="random_move":
                ins=random.randrange(0,int(command[1]))
                pt.moveTo(float(cmd.split_text(command[2+ins])[0]),float(cmd.split_text(command[2+ins])[1]))
            if command[0] =="run":
                running=command[1]
                macro.run_code(project_json["macro"]["commands"][command[1]])
            if command[0]=="anchor":
                pass
            if command[0]=="return":
                ins=project_json["macro"]["commands"][running]
                macro.run_code(ins[ins.index("anchor %s" %command[1]):])
            if command[0]=="console":
                cmd.console(command[1])
            if command[0]=="till":
                wh=True
                if command[1]=="img":
                    while wh:
                        ins=pt.locateOnScreen("projects\\%s\\imgs\\%s" %(project_name,project_json["macro"]["imgs"][command[2]]), confidence=settings['confidence'], grayscale=True)
                        if ins is not None:
                            macro.run_code([command[3]])
                            wh=False
            if command[0]=="img_ifs":
                wh=True
                while wh:
                    for r in range(1,int(command[1])+1,1):
                        ins=pt.locateOnScreen("projects\\%s\\imgs\\%s" %(project_name,project_json["macro"]["imgs"][command[(r*2)]]), confidence=settings['confidence'], grayscale=True)
                        if ins is not None:
                            macro.run_code([command[r*2+1]])
                            wh=False
            if command[0]=="end":
                break
            if command[0]=="pass":
                pass
            if command[0]=="limbus_stage_rand":
                wh=True
                while wh:
                    rand=random.randrange(int(command[2])*-1, int(command[2]))
                    pt.moveTo(x=int(cmd.split_text(command[1])[0])+rand,y=int(cmd.split_text(command[1])[1])+rand)
                    time.sleep(0.05)
                    pt.click()
                    time.sleep(0.1)
                    ins=pt.locateOnScreen("projects\\%s\\imgs\\%s" %(project_name,project_json["macro"]["imgs"][command[3]]), confidence=settings['confidence'], grayscale=True)
                    if ins is not None:
                        wh=False
                        pt.moveTo(ins)
            if command[0]=="var":
                if command[1]=="set":
                    project_vars[command[2]]=int(command[3])
                if command[1]=="if":
                    if cmd.compare_as_var(project_vars[command[2]],command[4],command[3]) == True:
                        macro.run_code(cmd.split_text([command[5]]))
                    else:
                        macro.run_code(cmd.split_text([command[6]]))
                if command[1]=="compare":
                    if cmd.compare_as_var(project_vars[command[2]],project_vars[command[4]],command[3]) == True:
                        macro.run_code(cmd.split_text([command[5]]))
                    else:
                        macro.run_code(cmd.split_text([command[6]]))
                if command[1]=='cal':
                    pass
            if command[0]=="rand_area":
                insx=random.randint(int(command[1]), int(command[2]))
                insy=random.randint(int(command[3]), int(command[4]))
                pt.moveTo(insx, insy)
                    


settings=cmd.read_file("settings.json")
project_name=pt.prompt(text="실행할 프로젝트 이름을 입력하세요.",title="Project Name",default=settings["default_project"])
if project_name!="":
    if cmd.find_file("projects\\%s" %project_name) ==True:
        project_json = cmd.read_file("projects\\%s\\main.json" %project_name)
        cmd.console("vars settings...")
        project_vars=project_json["vars"]
        print(project_vars)
        cmd.console("macro now run!")
        running=settings["start_command"]
        macro.run_code(project_json["macro"]["commands"][running])
        #macro.run_code(["mouse_to_img prisoner_1"])
    else:
        cmd.console("no Project Found Named %s" %project_name)
else:
    cmd.console("No Project Name.")
