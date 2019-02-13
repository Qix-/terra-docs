# Some code
```c
/* Some C code! */
int foo = 10;
```

```lua
-- Some Lua code
local foo = 10
```

```terra
-- Some terra code
local foo: int = 10
local someString: &int8 = 'This is a string!'

terra bar():int
    return foo -- yes I know this doesn't work
end
```
