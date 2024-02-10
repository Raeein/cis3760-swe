export default function SearchBar({ onSearched }) {
  return (
    <div className="SearchContainer">
      <input
        className="SearchBar"
        type="text"
        placeholder="Search..."
        onChange={onSearched}
      />
      {/* <button type="submit">Search</button> */}
    </div>
  );
}
