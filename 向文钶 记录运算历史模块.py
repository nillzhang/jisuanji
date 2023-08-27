def clean_history():
    global frame_inner
    global frame_right
    global history_label_obj_list
    history_label_obj_list = []
    with open('history.pkl', 'wb') as f:
        pickle.dump(history_label_obj_list, f)
    frame_right.destroy()
    frame_right = tkinter.Frame(window, width=200)
    tkinter.Label(frame_right, text="运算历史", font=("Arial", 14, "underline bold")).pack()
    frame_inner = tkinter.Frame(frame_right)
    frame_inner.pack(fill="x", side="top")
    cls_button = tkinter.Button(frame_right, text="清空", command=lambda: clean_history())
    cls_button.pack(fill="x", side="top")
    print('....')
def display(history_label_obj_list):
    for h in history_label_obj_list:
        frame_right.pack()
        # 将算式记录显示出来
        t = tkinter.Label(frame_inner, text=h, background="seashell")
        t.pack()
cls_button = tkinter.Button(frame_right, text="清空", command=lambda: clean_history())
cls_button.pack(fill="x", side="top")
window.after(0, display(history_label_obj_list=history_label_obj_list))
window.mainloop()