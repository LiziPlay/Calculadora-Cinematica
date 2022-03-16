magnitudes = {"x", "t", "v"}
unidades_x = ["mm", "cm", "dm", "m", "dam", "hm", "km"]
unidades_t = ["s", "min", "h"]
target = ""


def converse(m, u, u_2):
    if "/" in u:
        u_x1, u_t1 = u.split("/")
        u_x2, u_t2 = u_2.split("/")
        a_x = m * 10 ** -(unidades_x.index(u_x1) - unidades_x.index(u_x2))
        a_t = m * 60 ** -(unidades_t.index(u_t1) - unidades_t.index(u_t2))
        return m * a_t / a_x
    elif u in unidades_x:
        a = unidades_x.index(u) - unidades_x.index(u_2)
        return m * 10 ** a
    elif u in unidades_t:
        a = unidades_t.index(u) - unidades_t.index(u_2)
        return m * 60 ** a
    else:
        print("unidad no existente")


def mru_equation(x, u_x, t, u_t, v, u_v):
    global target
    u_vx, u_vt = u_v.split("/")
    if x == "x":
        target = u_x
        v = converse(v, f"{u_vx}/{u_vt}", f"{u_x}/{u_t}")
        return v * t
    elif t == "t":
        target = u_t
        v = converse(v, f"{u_vx}/{u_vt}", f"{u_x}/{u_t}")
        return x / v
    elif v == "v":
        target = u_v
        x = converse(x, u_x, u_vx)
        t = converse(t, u_t, u_vt)
        return x / t
    else:
        print("Incognita no reconocida")


def greet():
    print(f"""           -----Calculadora Cinemática-----
  versión: 1.0.0      
  Bienvenido a la calculadora cinemática,
  intruduzca uno de los siguientes comandos:
        
    -converse (magnitud, unidad inicial, unidad final)
        
      magnitudes: {magnitudes}
      unidades espacio (x, u, u_2): {unidades_x}
      unidades tiempo (t, u, u_2): {unidades_t}
      velocidad (v, x/t, x/t2) IMPORTANTE SEPARAR POR '/'

      Ejemplos: 
      >> converse, 120, s, h --> 2h
      >> converse, 10, km, m --> 10000m
      >> converse, 10, m/s, km/h -->   

        
    -mru_equation (x, u_x, t, u_t, v, u_v)
      Sustituir cada magnitud por su valor e indicar su unidad en la 
      siguiente variable, dejar la incognita con su respectiva magnitud.
    
      magnitudes: {magnitudes}
      unidades espacio : {unidades_x}
      unidades tiempo ): {unidades_t}
      velocidad x/t IMPORTANTE SEPARAR POR '/'
        
      Ejemplos:
        >> mru_equation, 10, m, 2, s, v, m/s --> 5 m/s
        >> mru_equation, x, km, 3, min, 10, km/h --> 0.5 km
        >> mru_equation, 13, hm, t, h, 20, m/h --> 65 h
      """)



if __name__ == "__main__":
    greet()

    user = str(input()).replace(" ", "").split(",")

    if user[0] == "converse":
        user[1] = float(user[1])
        if int(user[1]) == user[1]:
            user[1] = int(user[1])
        print(converse(user[1], user[2], user[3]), user[3])

    elif user[0] == "mru_equation":
        try:
            user[1] = float(user[1])
        except:
            pass
        try:
            user[3] = float(user[3])
        except:
            pass
        try:
            user[5] = float(user[5])
        except:
            pass
    print(mru_equation(user[1], user[2], user[3], user[4], user[5], user[6]), target)
