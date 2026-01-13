function Header({ title, desc }: { title: string; desc: string }) {
  return (
    <>
      <h1 className="text-2xl text-center">{title}</h1>
      <p className="text-center">{desc}</p>
    </>
  );
}

export default Header;
