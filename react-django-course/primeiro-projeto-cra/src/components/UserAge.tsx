type Props = {
  age: number;
}

export const UserAge = (props: Props) => {
  return (
    <h4>Minha idade é: {props.age} anos</h4>
  );
}
