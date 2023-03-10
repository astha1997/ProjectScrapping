from fpdf import FPDF
from Scrapper import all_course, scrap_all, get_course
import boto3

s3 = boto3.client('s3')

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-northeast-1',
    aws_access_key_id='**************',
    aws_secret_access_key='******'
)



count=0
list_courses = all_course()
for i in list_courses:
        filename=i+'.pdf'
        pdf = FPDF()
        pdf.add_page()
        count+=1
        if filename=='Be A DevOps Pro Tech Neuron.pdf' or filename=='Salesforce Administrator.pdf' or filename=='Cyber Security Masters.pdf' or filename=='Tibco Business Works.pdf' or filename=='Cyber Security Foundations.pdf' or filename=='Explainable AI.pdf' or filename=='Be A DevOps Pro.pdf' or filename=='Youtube Mastery Course in Hindi Tech Neuron.pdf' or filename=='Cyber Security Masters Tech Neuron.pdf':
                continue
        print(filename)
        CourseName=get_course(i)['Course_title']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'CourseName',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = CourseName)
        #print('CourseName' ,CourseName)
            
        Description=get_course(i)['Description']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Description',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Description)
        #print('Description' ,Description)   

        Language=get_course(i)['Language']
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Language',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Language)
            
        Pricing=get_course(i)['Pricing'] 
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Pricing',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = str(Pricing))
            
        Curriculum_data=' '.join(get_course(i)['Curriculum_data'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Curriculum_data',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Curriculum_data)
            
        Learn=' '.join(get_course(i)['Learn'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Learn',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Learn)
            
        Requirements=' '.join(get_course(i)['Requirements'])
        pdf.set_font("Arial", size = 11)
        pdf.cell(200, 10,  txt = 'Requirements',ln = 1, align = 'L')
        #pdf.set_font("Arial", size = 9)
        pdf.multi_cell( 200,10,txt = Requirements)
               
               
                
        # save the pdf with name .pdf
        pdf.output(filename)
        s3.Bucket('scrapfiles').upload_file(Filename=filename, Key=filename)
        #To stop at 50 files as no of files were huge
        if(count>=50):
                break
    
    
