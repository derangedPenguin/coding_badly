import styles from "./page.module.css";

function Button({val}) {
  return <button>{val}</button>;
}

function Header() {
  return (
    <div className="header">
      <h1>Golf Analyzer</h1>
      <h2>hi</h2>
    </div>
  );
}

function AnalyzerForm() {
  <form>
    
  </form>
}

export default function Home() {
  return (
  <>
    <Header />

    <Button val={"1"}/>
    <Button val={"2"} />
  </>  );
}
