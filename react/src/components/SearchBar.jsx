export default function SearchBar({ onSearched }) {
  return (
    <input
      className="search-bar"
      type="text"
      placeholder="search for a job..."
      onChange={onSearched}
    />
  );
}
