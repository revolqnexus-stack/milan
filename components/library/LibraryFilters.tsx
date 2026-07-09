"use client";

import { useState } from "react";

const CHIPS = [
  { id: "all", label: "All packs" },
  { id: "gnm", label: "GNM" },
  { id: "year1", label: "1st Year" },
  { id: "year2", label: "2nd Year" },
  { id: "year3", label: "3rd Year" },
  { id: "unlocked", label: "My packs" },
  { id: "locked", label: "Locked" },
];

export function LibraryFilters({
  onFilter,
}: {
  onFilter?: (id: string) => void;
}) {
  const [active, setActive] = useState("all");

  function select(id: string) {
    setActive(id);
    onFilter?.(id);
  }

  return (
    <div className="sb-chips" role="group" aria-label="Filter packs">
      {CHIPS.map((chip) => (
        <button
          key={chip.id}
          type="button"
          className={`sb-chip${active === chip.id ? " active" : ""}`}
          onClick={() => select(chip.id)}
          aria-pressed={active === chip.id}
        >
          {chip.label}
        </button>
      ))}
    </div>
  );
}
