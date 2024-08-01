# TokenOculto
Esse script serve para identificar e validar o token exposto e explorar o mesmo, simulei um ataque de XSS que rouba o token JWT armazenado em um campo de entrada oculto. O script vai tomar o URL de destino do usuário e injetar um script malicioso na página, caso haja uma vulnerabilidade XSS em algum campo de entrada.

* Requisitos:
  
  pip install requests beautifulsoup4
  
* Execução do arquivo e Identificação do token oculto:
   ![image](https://github.com/user-attachments/assets/249b09f3-c05b-4eaf-bc73-3e994eada92e)
