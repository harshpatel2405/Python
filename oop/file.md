# ServletConfig

---

## Definition

ServletConfig is an object provided by the Servlet container that is used to store and retrieve configuration information specific to a particular servlet.

---

## The Real Advantage of ServletConfig

It is **NOT**:

> "ServletConfig avoids redeployment."

It is:

> **ServletConfig separates configuration from application logic.**

---

## Important Methods

| Method | Work |
|---|---|
| `getInitParameter(String name)` | Gets the value of a specific parameter |
| `getInitParameterNames()` | Gets all parameter names |
| `getServletName()` | Gets the servlet name |
| `getServletContext()` | Gets the ServletContext object |

---

## Without ServletConfig vs With ServletConfig

| Point | Without ServletConfig | With ServletConfig |
|---|---|---|
| **1. Configuration** | Configuration is usually written directly in Java code. | Configuration is provided through `web.xml` using `init-param`. |
| **2. Code** | Simpler and requires less code. | Requires `ServletConfig` methods such as `getInitParameter()`. |
| **3. Maintainability** | Harder to maintain when configuration values increase. | Easier to maintain because configuration is separated from Java code. |
| **4. Scope** | No servlet-specific configuration mechanism. | Configuration is **specific to one servlet**. |
| **5. Change / Reload** | Changing a hardcoded value means changing Java code and rebuilding/reloading. | Changing `web.xml` changes the servlet's configuration; the application/servlet still needs to reload for the new configuration to take effect. |

---

## Old Application

In older Servlet applications, configuration was commonly written in `web.xml`.

```xml
<servlet>
    <servlet-name>Login</servlet-name>
    <servlet-class>LoginServlet</servlet-class>
    <init-param>
        <param-name>email</param-name>
        <param-value>admin@gmail.com</param-value>
    </init-param>
</servlet>

<servlet>
    <servlet-name>Signup</servlet-name>
    <servlet-class>SignupServlet</servlet-class>
    <init-param>
        <param-name>email</param-name>
        <param-value>admin@gmail.com</param-value>
    </init-param>
</servlet>

<!-- and more servlets... -->
```

### Flow

```text
web.xml
   ↓
init-param
   ↓
ServletConfig
   ↓
Servlet
```

---

## Modern Application

Modern Servlet applications can use annotations instead of putting servlet-specific initialization parameters in `web.xml`.

```java
@WebServlet(
    urlPatterns = "/login",
    initParams = {
        @WebInitParam(
            name = "email",
            value = "admin@gmail.com"
        )
    }
)
public class LoginServlet extends HttpServlet {

}
```

### Flow

```text
@WebServlet + @WebInitParam
          ↓
    ServletConfig
          ↓
       Servlet
```

---

## Key Point

**`web.xml` and `ServletConfig` are not the same thing.**

- `web.xml` → One way to define servlet configuration.
- `@WebServlet` / `@WebInitParam` → Annotation-based way to define servlet configuration.
- `ServletConfig` → Used by the servlet to access its configuration.

### Easy Memory Trick

```text
ServletConfig
      ↓
Configuration of ONE servlet

ServletContext
      ↓
Configuration / data for the WHOLE application
```
