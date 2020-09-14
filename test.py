import pycurl

pc = pycurl.Curl()
pc.setopt(pycurl.POST, 1) # POST method
pc.setopt(pycurl.URL, 'http://example.com/webservice/upload/') # 上传的API接口
pc.setopt(pycurl.HTTPPOST, [('file1', (pc.FORM_FILE, '/path/to/your/imagefile'))]) # 设置POST方法的参数
pc.perform() # Actually do POST request, 文件上传
pc.close()