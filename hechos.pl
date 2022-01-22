
verificacion(si,aceptado).
verificacion(no,rechazado).
pregunta(1,'Es solvente economicamente').
pregunta(2,'Tiene trabajo estable').
pregunta(3,'Tiene deudas').
pregunta(4,'Es mayor de edad').
pregunta(5,'Tiene propiedades').
pregunta(6,'Cuenta con un garante').

pregunta(7,'Es solvente economicamente').
pregunta(8,'Tiene trabajo estable').
pregunta(9,'Tiene deudas').
pregunta(10,'Es mayor de edad').
pregunta(11,'Tiene propiedades').
pregunta(12,'Es familiar').

problema(1,'No es solvente economicamente').
problema(2,'No tiene un trabajo estable').
problema(3,'Tiene deudas').
problema(4,'Es menor de edad').
problema(5,'No cuenta con propiedades').
problema(6,'No cuenta con un garante').
problema(7,'El garante no es solvente economicamente').
problema(8,'El garante no tiene trabajo estable').
problema(9,'El garante tiene deudas').
problema(10,'El garante es menor de edad').
problema(11,'El garante no tiene propiedades').
problema(12,'El garante no es un familiar').


solvente(X,R):-verificacion(X,R).
trabajoe(X,R):-verificacion(X,R).
deudas(X,R):-verificacion(X,R).
mayor(X,R):-verificacion(X,R).
casado(X,R):-verificacion(X,R).
propietario(X,R):-verificacion(X,R).
historial(X,R):-verificacion(X,R).
garante(X,R):-verificacion(X,R).
familiar(X,R):-verificacion(X,R).

candidato(P1,P2,P3,P4,P5,P6,R):-solvente(P1,R), trabajoe(P2,R),not(deudas(P3,R)),
                               mayor(P4,R),propietario(P5,R),garante(P6,R).
cgerente(P1,P2,P3,P4,P5,P6,R):-solvente(P1,R), trabajoe(P2,R),not(deudas(P3,R)),
                               mayor(P4,R),propietario(P5,R),familiar(P6,R).



obprestamo(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,R):- candidato(P1,P2,P3,P4,P5,P6,R),
                                                    cgerente(P7,P8,P9,P10,P11,P12,R).

obprestamo(_P1,_P2,_P3,_P4,_P5,_P6,_P7,_P8,_P9,_P10,_P11,_P12,'rechazado').