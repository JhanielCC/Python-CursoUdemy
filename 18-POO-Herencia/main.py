import clases


persona = clases.Persona()
persona.setNombre("Usuario")
persona.setApellidos("Apellidos Us")
persona.setAltura("165cm")
persona.setEdad("500 años")

print(f"La persona es:  {persona.getNombre()} {persona.getApellidos()}")
#print(persona.hablar())
print("____________________________________________________")


informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Apellidos Infor")
print(f"La persona es:  {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("____________________________________________________")
tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
print(tecnico.getLenguajes()) #El constructor del padre no se ejecuta en el hijo