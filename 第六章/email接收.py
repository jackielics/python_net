#代码6-13ema106,py 
#!/usr/bin/env python
#coding:utf-8
import poplib
from email.parser import Parser 
from email.header import decode_header 
from email.utils import parseaddr 
def decode_str(s):
    (value,charset)=decode_header(s)[0]
    if charset:
        value=value.decode(charset)
    return value
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type=msg.get('Content-Type',).lower()
        pos=content_type.find('charset =')
        if pos>=0:
            charset = content_type[pos+8:].strip()
    return charset
def show_header(msg):
    for header in ['From','To','Subject']:
        value=msg.get(header,'')
        if value:
            if header=='Subject':
                value = decode_str(value)
            else:
                (hdr,addr)=parseaddr(value)
                name = decode_str(hdr)
                addr = decode_str(addr)
                value=u'%s<%s>'%(name,addr)
        print('%s:%s' % (header,value))
def show_body(msg):
    if (msg.is_multipart()):
        parts=msg.get_payload()
        for part in parts:
            show_body(part)
    else:
        content_type=msg.get_content_type()
        print('content type=',content_type)
        type_pre=content_type.split('/')[0]
        if type_pre=='text':
            content =msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print(content)
        elif type_pre=='image':
            fname=msg['Content-ID']+'.'+content_type.split('/')[1]
            p_file=open(fname,'wb')
            data=msg.get_payload(decode=True)
            p_file.write(data)
            p_file.close()
            print('A picture is downloaded to',fname)
        else:
            fname = msg.get_filename()
            fname = decode_str(fname)
            att_file=open(fname,'wb')
            data=msg.get_payload(decode=True)
            att_file.write(data)
            att_file.close()
            print('The attachment is downloaded to',fname)

host="pop.qq.com"
user="642825572"
code="ecruzodsmxqrbdhj"
pop_obj=poplib.POP3_SSL(host)
print(pop_obj.getwelcome())
pop_obj.user(user)
pop_obj.pass_(code)
print('Messages:%s,Size:%s'%pop_obj.stat())
(resp,mails,octets)=pop_obj.list()
index=len(mails)
print('index =', index)
(resp,lines,octets)=pop_obj.retr(index)
lines_str=[]
for xx in lines:
    lines_str.append(xx.decode('utf-8'))
msg_content ='\n'.join(lines_str)
msg = Parser().parsestr(msg_content)
show_header(msg)
show_body(msg)
pop_obj.quit()