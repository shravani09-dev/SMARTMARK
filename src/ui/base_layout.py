import streamlit as st


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
            background:#5865F2 !important;
            padding:10px,20px !important;
            color:white !important;
            border:None !important;
            transition:transform 0.25s ease-in-out !important;
        }
                
        button[kind=secondary]{
            border-radius:1.5rem !important;
            background:#EB459E !important;
            padding:10px,20px  !important;
            color:white !important;
            border:None !important;
            transition:transform 0.25s ease-in-out !important;
        }
                
        button[kind=ternary]{
            border-radius:1.5rem !important;
            background:#black !important;
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