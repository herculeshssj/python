// Tentando declarar propTypes para o componente UserEmail de um modo diferente
type EmailProps = {
  email: string;
}

export const UserEmail = (email: EmailProps) => {
  return (
    <h4>Meu email é: {email.email} </h4>
  );
}