import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

'''
邮件发送需要包含哪些内容：
发送邮件使用的协议（建立链接）、主题、发件人、收件人、正文、附件
'''


class SendEmail:
    def send_mail(self, filename):
        msg = email.mime.multipart.MIMEMultipart()  # 生成包含多个邮件体的对象

        msg['from'] = 'flyyujunmh@163.com'
        msg['to'] = 'flyyujunmh@163.com'
        msg['subject'] = "自动化测试报告"
        content = '''
        Hi all，
        自动化测试报告，请见附件
        官网：http://xqtesting.sxl.cn
        博客：http://xqtesting.blog.51cto.com
        微信公众号：测试帮日记
        带附件
        '''

        # 邮件正文
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)

        # excel附件
        xlsxpart = MIMEApplication(open(filename, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(xlsxpart)

        # jpg图片附件
        jpgpart = MIMEApplication(open('weixin.jpg', 'rb').read())
        jpgpart.add_header('Content-Disposition', 'attachment', filename='weixin.jpg')
        msg.attach(jpgpart)

        # 发送邮件
        smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)  # 设置为调试模式，console中显示
        smtp.connect('smtp.163.com', '25')  # 链接服务器，smtp地址+端口
        smtp.login('flyyujunmh@163.com', '***198731545***')  # 登录，用户名+密码
        smtp.sendmail('flyyujunmh@163.com', 'flyyujunmh@163.com', str(msg))  # 发送，from+to+内容
        smtp.quit()


#mail = SendMail()
#mail.send_mail('小强python全栈自动化测试培训班的问候')