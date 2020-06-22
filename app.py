# CREATED BY MUHAMMAD HANAN ASGHAR
# PYTHONIST
from tkinter import *
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0


# Function Here

def startDownload(url):
    global file_size
    path = askdirectory()
    if path is None:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()
        file_size = st.filesize
        st.download(output_path=path)
        btn_entry['text'] = "Downloaded"
    except Exception as e:
        print(e)
        print("Something Went Wrong")

def downloadBtn():
    try:
        btn_entry['text'] = "Downloading...."
        btn_entry['state'] = 'disabled'
        url = link_entry.get()
        if url == " ":
            return
        else:
            thread = Thread(target=startDownload,args=(url,))
            thread.start()
    except Exception as e:
        print(e)


root = Tk()
root.iconbitmap('icon.ico')
root.geometry("400x500")
root.title("Youtube Downloader in Python")
# Frame
main_frame = Frame(root,bg = "white")
main_frame.place(x=0,y=0,height = 500,width = 400)
# Image
file = PhotoImage(file="youtube.png")
headingIcon = Label(main_frame,image=file)
headingIcon.grid(row=0,column = 0,pady=3)
link_entry = Entry(main_frame,bd=4,relief="groove")
link_entry.grid(padx = 30,pady = 20,ipadx=100,ipady = 8,row=1,column = 0)
btn_entry = Button(main_frame,text="Download",bd = 4,relief="flat",command=downloadBtn)
btn_entry.grid(row = 2,column = 0,ipady = 5,ipadx = 15)
root.mainloop()