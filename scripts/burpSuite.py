from burp import IBurpExtender, IHttpListener, IInterceptedProxyMessage

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set the extension name
        callbacks.setExtensionName("Simple Python Extension")
        
        # Register the HTTP listener
        callbacks.registerHttpListener(self)
        
        print("Extension loaded successfully!a")
    
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            request = messageInfo.getRequest()
            analyzedRequest = self._helpers.analyzeRequest(request)
            headers = analyzedRequest.getHeaders()
            
            # Modify headers as needed
            new_headers = []
            for header in headers:
                if header.startswith("User-Agent:"):
                    new_headers.append("User-Agent: CustomUserAgent")
                else:
                    new_headers.append(header)
            
            # Rebuild the request with modified headers
            body = request[analyzedRequest.getBodyOffset():]
            new_message = self._helpers.buildHttpMessage(new_headers, body)
            messageInfo.setRequest(new_message)

            print("Modified request headers")

