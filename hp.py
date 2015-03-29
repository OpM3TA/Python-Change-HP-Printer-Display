import os,sys,socket

printer = socket.socket()

"""
Perl stuff ->
\e%-12345X\@PJL JOB
\@PJL RDYMSG DISPLAY="Hello"
\@PJL EOJ
\e%-12345X

UEL = chr(0x1B)+chr(0x25)+chr(0x2D)+chr(0x31)+chr(0x32)+chr(0x33)+chr(0x34)+chr(0x35)+chr(0x58)
buf = UEL + '...@PJL RDYMSG DISPLAY = "%s"\n' % (message) + UEL + "\n"

"""
def create_payload(display_msg):
    if len(display_msg) >16:
        print "Message is too long! Keep it under 16 characters."
        print "Your message was "+str(len(display_msg))+" characters"
        return ""
    else:
        stage1="\x1b%-12345X@PJL JOB\r\n"
        stage2='@PJL RDYMSG DISPLAY="'+display_msg+'"\r\n'
        stage3="@PJL EOJ\r\n"
        end = "\x1b%-12345X\r\n"
        return stage1+stage2+stage3+end


payload= create_payload(raw_input("Display Message: "))
print payload
# printer_host = raw_input("Enter the IP Address of the printer: ")
# printer.connect((printer_host, 9100))

# Let's hope this works

# printer.send(payload)
# printer.close()
