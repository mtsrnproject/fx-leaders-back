// here we just define the obj for proxies that give the address and make proxy with address per every microservice 


// all dependencies that we need
const {
    createProxyMiddleware,
    debugProxyErrorsPlugin, // subscribe to proxy errors to prevent server from crashing
    loggerPlugin, // log proxy events to a logger (ie. console)
    errorResponsePlugin, // return 5xx response on proxy error
    proxyEventsPlugin, // implements the "on:" option
    fixRequestBody
  } = require('http-proxy-middleware');
 


// required plugins for proxy middleware
const plugins = [debugProxyErrorsPlugin, loggerPlugin, errorResponsePlugin, proxyEventsPlugin]



//  main class for define the proxies by giving address
class proxies{

    proxy(address){                           // proxing the routes to specific service with the address
        return createProxyMiddleware({
            target:  address,
            changeOrigin: true,
            pathRewrite: {
              [`^/users`]: "",
            },
            plugins : plugins
          })
    }
}



module.exports = proxies



