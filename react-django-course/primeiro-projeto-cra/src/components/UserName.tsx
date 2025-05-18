export const UserName = () => {

  let name = "João da Silva";
  let names = {nome1: 'João da Silva', nome2: 'Maria da Silva', nome3: 'José da Silva'};
  
  const formatName = (value: string) => {
    return value.toUpperCase();
  }

  const nomeMaiusculo = (value: string) => value.toUpperCase();

  return (
    <>
    <h4>Meu nome é: {name} </h4>
    <h4>Meu nome é: {names.nome2} </h4>
    <h4>Meu nome é: { formatName(name) } </h4>
    <h4>Meu nome é: { nomeMaiusculo(name) } </h4>
    </>
  );
}