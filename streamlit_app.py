from ast import IsNot
from cgi import test
from curses import keyname
from doctest import DebugRunner
from email.mime import image
from itertools import count
from logging import PlaceHolder
#from turtle import home
from numpy import average, empty, true_divide
import pandas as pd
import streamlit as st
from PIL import Image
#from turtle import home
#import tkinter as TK
#import _tkinter
import http.client

conn = http.client.HTTPConnection("nocodb-v91-10.herokuapp.com")

headers = { 'xc-auth': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNhYnJ5NHVAZ21haWwuY29tIiwiZmlyc3RuYW1lIjpudWxsLCJsYXN0bmFtZSI6bnVsbCwiaWQiOiJ1c19oN3dsOWZtZXFqNjdnbSIsInJvbGVzIjoidXNlcixzdXBlciIsInRva2VuX3ZlcnNpb24iOiIwNjhiYjIxMGQxZjQwODc2ZTBjNTkzZDg1MzE3YzcwNDQ2OGRiZWNjODMyMzJmNTU0MzU2ZmNkNDhmOWYxN2Q3YmY3YzIxNTE0YWQ1OTBkNiIsImlhdCI6MTY1NjI3NTI4MH0.6RNj4xqm24Mjq7oplKwRrOulW2haC3fICeGc8QVp9bE" }

conn.request("GET", "/api/v1/db/data/noco/p_t9xx7wmf8gx9zk/Teams/views/Teams?limit=25&offset=0&where=", headers=headers)

res = conn.getresponse()
data = res.read()


image = Image.open('Ecasa.jpg')
lvl_rtng = [1,2,3,4,5]

def main():
    st.image(image)
    #st.title("E-CASA")

    nav = st.sidebar.radio("Menu",["Home","Data Manager","Data Visual"])

    ## Standing up the home page

    if nav == "Home":
        st.subheader("What is E-CASA?")
        st.markdown("E-CASA stands for "+"""<b style="font-size:20px">"Employee Competencies And Skills Analyzer"</b>"""+". This is the tool for people leaders to manage their team members competencies, impacted Dreyfus score, Skills towards business goals as well leadership goals. It will change the way we assess our team and build our team for better. It provides an objective way of helping our team to grow better.",unsafe_allow_html=True)

        st.subheader("Who is it for?")
        st.write("E-CASA is specifically designed for the people managers.")

        st.subheader("How to use?")
        st.markdown('1. E-CASA needs data to analyze')
        st.markdown('2. Use _**Data Entry**_ page under *Data Manager* to enter data')
        st.markdown('3. Use _*Data Search*_ page under *Data Manager* to search for specific data')
        st.markdown('4. Use _*Data Visual*_ page under *ANALYZE* your data')

    #Standing up the Data Manager Page

    elif nav == "Data Manager":
        st.subheader("Data Manager")
        
        ## Initializations for this page
        df = pd.read_excel("ECASA-DB.xlsx")
        drey_score = 1
        bsg_score = 1
        lsg_score = 1

        dm_submenu = ["Entry","Search","Modify","Delete"]
        dm_choice = st.sidebar.selectbox("Data Manager Menu",dm_submenu)

        if dm_choice == "Entry":
            st.markdown("""<h3 style="text-align:center;text-decoration: underline">Entry Form</h3>""",unsafe_allow_html=True)

            
            with st.form("de_form",clear_on_submit=False):
                col1,col2,col3 = st.columns([1,1,1])

                # setting columns for Employee ID, Employee Name, Timeline and Chapters

                with col1:
                    empid = st.text_input("Employee ID",key="empid_k")
                    timeline = st.selectbox("Timeline",["2022 Q1","2022 Q2","2022 Q3","2022 Q4"],key="timeline_k")

                with col2:
                    empname = st.text_input("Employee Name",key="empname_k")
                    chapter = st.selectbox("Chapter",["Chapter 1","Chapter 2","Chapter 3","Chapter 4"],key="chapter_k")

                with col3:
                    v_spacer(height=6, sb=False)
                    paygrd = st.selectbox("Pay Grade",["PG5","PG6","PG7","PG8","PG9"],key="paygrd_k")

                st.markdown("""<hr style="height:3px;border:none;color:#706d9e;background-color:#706d9e;" /> """, unsafe_allow_html=True)

                # setting columns for Dreyfus competencies
                col4,col5,col6 = st.columns([1,1,1])
                with col4:
                    v_spacer(height=4, sb=False)
                    bgpic = st.select_slider("Big Picture",lvl_rtng,key='bgpic_k')
                    devops = st.select_slider("Devops",lvl_rtng,key='devops_k')
                    prfsnl = st.select_slider("Professional",lvl_rtng,key='prfsnl_k')
                    test_skill = st.select_slider("Test",lvl_rtng,key='test_k')

                with col5:
                    st.markdown("""<h4 style="text-align:center;font-style:italic">Competencies</h3>""",unsafe_allow_html=True)
                    data_skill = st.select_slider("Data",lvl_rtng,key='data_k')
                    inrsrc = st.select_slider("Inner Source",lvl_rtng,key='inrsrc_k')
                    secrty = st.select_slider("Security",lvl_rtng,key='secrty_k')
                    awow = st.select_slider("AWOW",lvl_rtng,key='awow_k')

                with col6:
                    v_spacer(height=4, sb=False)
                    design = st.select_slider("Design",lvl_rtng,key='design_k')
                    infra = st.select_slider("Infrastructure",lvl_rtng,key='infra_k')
                    tech = st.select_slider("Tech",lvl_rtng,key="tech_k")
                    v_spacer(height=2, sb=False)
                    #de_drey_calc = st.form_submit_button(label="Calculate Dreyfus")

                #st.success("Dreyfus score: "+format(drey_score,".2f"))

                st.markdown("""<hr style="height:3px;border:none;color:#706d9e;background-color:#706d9e;" /> """, unsafe_allow_html=True) 

                # --------- Skills section creation ---------------
                col7,col8,col9 = st.columns([1,1,1])
                with col7:
                    v_spacer(height=4, sb=False)
                    bsg1 = st.select_slider("Business Goal 1",lvl_rtng)
                    lsg1 = st.select_slider("Play to win",lvl_rtng)

                with col8:
                    st.markdown("""<h4 style="text-align:center;font-style:italic">Skills</h3>""",unsafe_allow_html=True)
                    bsg2 = st.select_slider("Business Goal 2",lvl_rtng)
                    lsg2 = st.select_slider("Get better everyday",lvl_rtng)

                with col9:
                    v_spacer(height=4, sb=False)
                    bsg3 = st.select_slider("Business Goal 3",lvl_rtng)
                    lsg3 = st.select_slider("Succeed Together",lvl_rtng)
                    
                st.markdown("""<hr style="height:3px;border:none;color:#706d9e;background-color:#706d9e;" /> """, unsafe_allow_html=True)  

                # --------- Scores section creation ---------------
                placeholder_scores = st.empty()


                # Button for saving data and calculating scores
                col13,col14 = st.columns([1,2])
                with col13:
                    de_submit = st.form_submit_button(label="Save Data")
                with col14:
                    de_bsg_lsg_calc = st.form_submit_button(label="Calculate Scores")

                # --------- Button press action ---------------
                if de_bsg_lsg_calc:
                    calc_return = de_entry_calc(bgpic,data_skill,devops,design,inrsrc,infra,prfsnl,secrty,tech,test_skill,awow,bsg1,bsg2,bsg3,lsg1,lsg2,lsg3)
                    i=1
                    for val in calc_return:
                        if i == 1:
                            drey_score = val
                        elif i == 2:
                            bsg_score = val
                        else:
                            lsg_score = val
                        i = i+1
                
                with placeholder_scores.container():
                    draw_scores(drey_score,bsg_score,lsg_score)

                if de_submit:
                    drey_score = 0.25*float(tech)+0.25*float(design)+(0.5*average([(float(bgpic),float(devops),float(prfsnl),float(test_skill),float(data_skill),float(inrsrc),float(secrty),float(awow),float(infra))]))
                    bsg_score = average([float(bsg1),float(bsg2),float(bsg3)])
                    lsg_score = average([float(lsg1),float(lsg2),float(lsg3)])

                    new_data = {"Quarter":timeline,"Chapter":chapter,"Emp ID":empid,"Emp Name":empname,"Paygrade":paygrd,"Big Picture":int(bgpic),"Data":int(data_skill),"Design":int(design),"Devops":int(devops),"Inner Source":int(inrsrc),"Infrastructure":int(infra),"Professional":int(prfsnl),"Security":int(secrty),"Tech":int(tech),"Testing":int(test_skill),"AWOW":int(awow),"Dreyfus":float(drey_score),"Buiz Goal-1":int(bsg1),"Buiz Goal-2":int(bsg2),"Buiz Goal-3":int(bsg3),"BSG":float(bsg_score),"P2W":int(lsg1),"GBE":int(lsg2),"ST":int(lsg3),"LSG":float(lsg_score)}
                    st.info("Your data has been saved successfully")
                    st.info(data.decode("utf-8"))
                    df = df.append(new_data,ignore_index=True)
                    df.to_excel("ECASA-DB.xlsx",index=False)



        elif dm_choice == "Search":
            st.markdown(""" <h3 style="text-align:center">Search</h3>""",unsafe_allow_html=True)

            with st.form("de_search"):
                col1,col2,col3 = st.columns([1,1,1])
                with col1:
                    srch_id = st.text_input("Employee ID")
                with col2:
                    srch_chptr = st.multiselect("Chapter",["Chapter 1","Chapter 2","Chapter 3","Chapter 4"])
                    de_search = st.form_submit_button(label="Search Record")
                with col3:
                    srch_qrtr = st.multiselect("Timeline",["2022 Q1","2022 Q2","2022 Q3","2022 Q4"])
            
            if de_search:
                df_srch = empty
                

                if srch_id != "":
                    if srch_chptr:
                        if srch_qrtr:
                            #st.write('I am in srch-1')
                            df_srch = df.loc[(df['Quarter'].isin(srch_qrtr)) & (df['Chapter'].isin(srch_chptr)) & (df['Emp ID'] == srch_id)]
                        elif not srch_qrtr:
                            #st.write('I am in srch-2')
                            df_srch = df.loc[(df['Chapter'].isin(srch_chptr)) & (df['Emp ID'] == srch_id)]
                    elif not srch_chptr:
                        if srch_qrtr:
                            #st.write('I am in srch-3')
                            df_srch = df.loc[(df['Quarter'].isin(srch_qrtr)) & (df['Emp ID'] == srch_id)]
                        elif not srch_qrtr:
                            #st.write('I am in srch-4')
                            df_srch = df.loc[(df['Emp ID'] == srch_id)]

                elif srch_id == "":
                    if srch_chptr:
                        if srch_qrtr:
                            #st.write('I am in srch-5')
                            df_srch = df.loc[(df['Quarter'].isin(srch_qrtr)) & (df['Chapter'].isin(srch_chptr))]
                        elif not srch_qrtr:
                            #st.write('I am in srch-6')
                            df_srch = df.loc[(df['Chapter'].isin(srch_chptr))]
                    elif not srch_chptr:
                        if srch_qrtr:
                            #st.write('I am in srch-7')
                            df_srch = df.loc[(df['Quarter'].isin(srch_qrtr))]
                        elif not srch_qrtr:
                            #st.write('I am in srch-8')
                            st.error('Please provide a valid field value to search!')
                else:
                    st.error('Something went wrong! Please contact support.')
                    
                if df_srch is empty:
                    st.write('')
                else:
                    st.write(df_srch)


        else:
            st.subheader("Contact Support")
            st.info("Are you looking for something? Please contact the support team at sup@test.com for any questions.")

    else:
        st.subheader("Contact Support")
        st.info("Are you looking for something? Please contact the support team at sup@test.com for any questions.")

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

def de_entry_calc(bgpic,data_skill,devops,design,inrsrc,infra,prfsnl,secrty,tech,test_skill,awow,bsg1,bsg2,bsg3,lsg1,lsg2,lsg3) -> None:
    drey_score = 0.25*float(tech)+0.25*float(design)+(0.5*average([(float(bgpic),float(devops),float(prfsnl),float(test_skill),float(data_skill),float(inrsrc),float(secrty),float(awow),float(infra))]))
    bsg_score = average([float(bsg1),float(bsg2),float(bsg3)])
    lsg_score = average([float(lsg1),float(lsg2),float(lsg3)])
    return(drey_score,bsg_score,lsg_score)

def draw_scores(drey_score,bsg_score,lsg_score):
    col10,col11,col12 = st.columns([1,1,1])
    with col10:
        v_spacer(height=4, sb=False)
        st.metric("Dreyfus Score",value=format(drey_score,".2f"))
    with col11:
        st.markdown("""<h4 style="text-align:center;font-style:italic">Scores</h3>""",unsafe_allow_html=True)
        st.metric("Business Skill Score",value=format(bsg_score,".2f"))
    with col12:
        v_spacer(height=4, sb=False)
        st.metric("Leadership skill score: ",value=format(lsg_score,".2f"))
    st.markdown("""<hr style="height:3px;border:none;color:#706d9e;background-color:#706d9e;" /> """, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
