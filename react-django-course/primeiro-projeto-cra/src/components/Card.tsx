import { ReactNode } from "react";

type Props = {
  children: ReactNode;
}

export const Card = ({ children }: Props) => {
  return (
    <div style={{ border: '1px solid red', padding: '16px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)' }}>
      {children}
    </div>
  );
}