import streamlit as st
from html import escape

def style_background_home():
    st.markdown('''
    
    <style>
        .stApp{
                background : #5865F2 ! important;
                }    

        .stApp div[data-testid="stColumn"]{
                background : #E0E3FF ! important;
                padding:2.5rem !important;
                border-radius: 5rem !important;
                } 
                
    </style>

    ''', unsafe_allow_html=True)



def style_background_dashboard():
    st.markdown('''
    
    <style>
                .stApp{
                     background:#E0E3FF !important;
                }
    </style>

    ''', unsafe_allow_html=True)


def style_base_layout():
    st.markdown('''
    
         
                  
    <style>
         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');


         /* Hide top bar of streamlit */       
        #Mainmenu, header, footer {
                visibility:hidden;
                }

        .block-container {
                padding-top:1.5rem !important;
                }

        h1{
           font-family: Climate Crisis, sans-serif   ! important;
           font-size:3.5rem ! important;
           line-height:1.1 ! important;    
           margin-bottom:0rem !important;
        }
                
        
        h2{
           font-family: 'Climate Crisis', sans-serif   ! important;
           font-size:1.5rem ! important;
           line-height:1.1 ! important;    
           margin-bottom:0rem !important;
        }
                
        h3,h3,p{
           font-family:'Outfit' , sans-serif !important;
        }
                
        button{
            border-radius:1.5rem !important;
            background-color:#5865F2 !important;
            padding:10px,20px !important;
            color:white !important;
            border:None !important;
            transition:transform 0.25s ease-in-out !important;
            
        }
                
        button[kind=secondary]{
            border-radius:1.5rem !important;
            background-color:#EB459E !important;
            padding:10px,20px  !important;
            color:white !important;
            border:None !important;
            transition:transform 0.25s ease-in-out !important;
        
        }
                
        button[kind=tertiary]{
            border-radius:1.5rem !important;
            background-color:#black !important;
            padding:10px,20px !important;
            color:white !important;
            border:None !important;
            transition:transform 0.25s ease-in-out !important;
        }
                
        button:hover{
            transform:scale(1.05)      
        }
                
        
                
       
               
                
    </style>

    ''', unsafe_allow_html=True)


def render_attendance_table(display_df):
    rows_html = []

    for _, row in display_df.iterrows():
        rows_html.append(
            "<tr>"
            f"<td>{escape(str(row['Time']))}</td>"
            f"<td>{escape(str(row['Subject']))}</td>"
            f"<td>{escape(str(row['Subject Code']))}</td>"
            f"<td>{escape(str(row['Attendance Stats']))}</td>"
            "</tr>"
        )

    st.markdown(
        f"""
        <div class="smartmark-attendance-table-card" style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:18px; overflow:hidden; margin-top:0.75rem;">
            <table class="smartmark-attendance-table" style="width:100%; border-collapse:collapse; color:#111827; font-family:'Noto Serif', serif;">
                <thead>
                    <tr style="background:#FFFFFF;">
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Time</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Subject</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; border-right:1px solid #E5E7EB; font-weight:600;">Subject Code</th>
                        <th style="text-align:left; padding:14px 16px; border-bottom:1px solid #E5E7EB; font-weight:600;">Attendance Stats</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows_html)}
                </tbody>
            </table>
        </div>
        <style>
            .smartmark-attendance-table td {{
                background:#FFFFFF;
                padding:14px 16px;
                border-bottom:1px solid #E5E7EB;
                border-right:1px solid #E5E7EB;
                color:#111827;
            }}

            .smartmark-attendance-table tbody tr:last-child td {{
                border-bottom:none;
            }}

            .smartmark-attendance-table td:last-child,
            .smartmark-attendance-table th:last-child {{
                border-right:none !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )