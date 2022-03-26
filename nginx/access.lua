local var1 = ngx.var[1]
ngx.log(ngx.ERR, "var1: "..var1)
local index = string.find(var1, ":")
if index ~= nil then
    ngx.var.myvar = "192.168.118.129:"..string.sub(var1,index + 1,string.len(var1))
end
ngx.log(ngx.ERR, "ngx.var.myvar: "..ngx.var.myvar)