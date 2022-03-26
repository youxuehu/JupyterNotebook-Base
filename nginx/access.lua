local var1 = ngx.var[1]

local index = string.find(var1, ":")
if index ~= nil then
    ngx.var.myvar = "notebook.net:"..string.sub(var1,index + 1,string.len(var1))
end
