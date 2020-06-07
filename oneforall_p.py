#!/usr/bin/python3
# coding=utf-8
import os
# get csv file name
def get_file_name(dir):
        # set dir name
        file_list = os.listdir(dir)
        filename_list = []
        for i in file_list:
                if "all_subdomain_result_" in i:
                        pass
                elif ".csv" in i and ".csv." not in i:
                        filename_list.append(i)
        return filename_list

# set html style
def set_html_style(filename):
        f1 = open(filename,"a+")
        html_style = '''
<html>
<head>
<style type="text/css">
table.hovertable {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    color:#333333;
    border-width: 1px;
    border-color: #999999;
    border-collapse: collapse;
}
table.hovertable th {
    background-color:#c3dde0;
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
table.hovertable tr {
    background-color:#d4e3e5;
}
table.hovertable td {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
a {
    color: #000000;
    font-size: 13px;
    }
a:visited {
    color: #8c8c8c;
    }
a:hover {
    color: #944dff;
}
</style>
</head>
<body>
<table class="hovertable">
<tr>
    <th>Url</th><th>Title</th><th>Banner</th><th>IP</th>
</tr>
        '''
        f1.write(html_style)
        f1.close()


# write data
def write_data(filename,data_list):
        data = '<tr onmouseover="this.style.backgroundColor=\'#ff6600\';" onmouseout="this.style.backgroundColor=\'#d4e3e5\';"><td><a href="'+data_list[0]+'" target=_blank style="font-weight:bold;">'+data_list[0]+'</a></td><td>'+data_list[1]+'</td><td>'+data_list[2]+'</td><td>'+data_list[3]+'</td></tr>\n'
        f2 = open(filename,"a+")
        f2.write(data)
        f2.close()


# read csv file all data
def read_data(filename):
        f3 = open(filename,"r",encoding='utf-8')
        f3_data = []
        for i in f3.readlines():
                i = i.strip("\n")
                f3_data.append(i)
        f3.close()
        return f3_data

def clear_data(data_list):
        new_dl = []
        for i in data_list:
                temp_list = i.split(",")
                newd = []
                newd.append(temp_list[6])
                # print(len(temp_list))
                # wait update
                newd.append(temp_list[15])
                newd.append(temp_list[16])
                newd.append(temp_list[10])
                new_dl.append(newd)
        return new_dl


def main():
        # get file name list
        fnl = get_file_name("results")
        for i in fnl:
                # filename i
                csv_file = "results/"+i
                # create html file
                html_file = "results/"+i+".html"
                set_html_style(html_file)
                new_data_list = clear_data(read_data(csv_file))
                new_data_list.pop(0)
                for j in new_data_list:
                        write_data(html_file,j)
        print("Success")

main()
